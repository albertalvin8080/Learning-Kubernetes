from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    NoEncryption,
)
from cryptography.x509.oid import NameOID
import datetime

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend(),
)

# Write private key to file
with open("./cert.d/albert.key", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=NoEncryption(),
        )
    )

common_name = "Albert Alvin"
organization = "DevInc"
# Create a CSR
csr = (
    x509.CertificateSigningRequestBuilder()
    .subject_name(
        x509.Name(
            [
                x509.NameAttribute(NameOID.COMMON_NAME, common_name),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            ]
        )
    )
    .sign(private_key, hashes.SHA256(), default_backend())
)

# Write CSR to file
with open("./cert.d/albert.csr", "wb") as f:
    f.write(csr.public_bytes(Encoding.PEM))

# Load CA key and certificate
with open("./cert.d/ca.key", "rb") as f:
    ca_private_key = serialization.load_pem_private_key(
        f.read(), password=None, backend=default_backend()
    )

with open("./cert.d/ca.crt", "rb") as f:
    ca_cert = x509.load_pem_x509_certificate(f.read(), default_backend())

validity = datetime.timedelta(1, 0, 0)
# validity = datetime.timedelta(0) # Causes `Unauthorized` error
# Sign the CSR with the CA key to create the certificate
cert = (
    x509.CertificateBuilder()
    .subject_name(csr.subject)
    .issuer_name(ca_cert.subject)
    .public_key(csr.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.today())
    .not_valid_after(datetime.datetime.today() + validity)
    .add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True,
    )
    .sign(ca_private_key, hashes.SHA256(), default_backend())
)

# Write certificate to file
with open("./cert.d/albert.crt", "wb") as f:
    f.write(cert.public_bytes(Encoding.PEM))

print("crt and key successfuly generated.")

# Explanation:
# Signing the Certificate Signing Request (CSR) with albert’s private key 
# and then signing the certificate with the CA’s private key are crucial 
# steps in the Public Key Infrastructure (PKI) process for a few reasons:

# >> Authentication: When albert signs the CSR with his private key, he is 
# providing a digital signature that proves the CSR was indeed created by him. 
# This is because only albert has the corresponding private key, and anyone 
# with the public key can verify that the signature is valid. This step ensures 
# that the CSR is authentic and has not been tampered with or forged.

# >> Integrity: The digital signature on the CSR also ensures the integrity of 
# the data within the CSR. If any of the information in the CSR were altered 
# after albert signed it, the signature would no longer be valid, and the CA 
# would know that the CSR had been tampered with.

# >> Non-repudiation: By signing the CSR, albert cannot later deny that he 
# created the CSR. This is important in scenarios where trust and accountability are critical.

# >> Authorization: When the CA signs the certificate using the CA’s private key, 
# it is essentially endorsing the information within the certificate and asserting 
# that it trusts the identity of the entity (albert, in this case). Anyone who 
# trusts the CA can now also trust the certificate issued to albert.

# >> Chain of Trust: The CA’s signature on the certificate establishes a chain 
# of trust from the CA to albert. This means that anyone who trusts the CA’s 
# certificate can extend that trust to albert’s certificate because it was signed by the CA.

# >> Security: The CA’s private key is usually kept in a highly secure environment
# to prevent unauthorized access. By signing certificates with this key, the CA 
# ensures that the certificates are issued in a controlled and secure manner.