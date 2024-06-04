from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from datetime import datetime, timedelta, timezone
import base64

server_ip = "172.23.93.189"  # IP assigned to the Ingress Object (probably the control plane's ip)
common_name = "myapp.com"  # host + domain defined inside Ingress Object (The common name is used to check if a certificate belongs to the intended entity)

# Using TLS 2.0 because TLS 3.0 doesn't support RSA encryption.
key = rsa.generate_private_key(
    # The public key in RSA consists of two parts: the public exponent and the modulus. The public exponent is used in the encryption process and signature verification.
    public_exponent=65537,
    key_size=2048,
    backend=default_backend(),
)

# >> x509.Name(): Creates a new Name object. The Name object represents an X.509 Distinguished Name (DN).
# A DN is consists of a sequence of relative distinguished names (RDN) where each RDN is expressed as
# an attribute type/value pair that can identify an entity uniquely within some scope.
# >> x509.NameAttribute(NameOID.COMMON_NAME, common_name): This is creating a NameAttribute object.
# A NameAttribute represents the individual attributes in a relative distinguished name (RDN). In this
# case, the attribute being created is a COMMON_NAME.
# >> NameOID.COMMON_NAME: This is an object identifier (OID) for the common name attribute. The common
# name is used to check if a certificate belongs to the intended entity and is often used to represent
# human-readable names such as `www.example.com`.
name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)])

# If not used, Chromium based browsers may complain about the self-signed certificate.
alt_names = [x509.DNSName(common_name), x509.DNSName(server_ip)]

# >> x509.BasicConstraints(ca=True, path_length=0): This is a constructor that creates a new
# BasicConstraints object. The BasicConstraints extension identifies whether the subject of
# the certificate is a Certificate Authority (CA) and the maximum depth of valid certification
# paths that include this certificate.
# >> ca=True: This indicates that the certificate is a CA certificate. A CA certificate is a
# kind of certificate that can issue other certificates. So, if ca=True, it means that the
# certificate can be used to issue other certificates.
# >> path_length=0: This is the maximum number of non-self-issued intermediate certificates
# that may follow this certificate in a valid certification path. A path length of 0 means
# that the CA certificate can only be used to issue end-entity certificates and not further CA certificates.
basic_constraints = x509.BasicConstraints(ca=True, path_length=0)
now = datetime.now(timezone.utc)

certificate = (
    x509.CertificateBuilder()
    .subject_name(name)
    .issuer_name(name) # Same as the subject because it's a self-signed certificate
    .public_key(key.public_key())
    .serial_number(1000)
    .not_valid_before(now)
    .not_valid_after(now + timedelta(days=365))
    .add_extension(basic_constraints, True)
    .sign(key, hashes.SHA256(), default_backend())
)

cert_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)
key_pem = key.private_bytes(
    encoding=serialization.Encoding.PEM, # PEM (Privacy Enhanced Mail) is a container file format often used to store cryptographic keys.
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption(),
)

# print(f"CERTIFICATE: {cert_pem}")
# print(f"PVKey: {key_pem}")

# with open("./cert.d/ingress_controller.crt", "wb") as f:
#     f.write(cert_pem)

# with open("./cert.d/ingress_controller.key", "wb") as f:
#     f.write(key_pem)

base64_cert_pem = base64.b64encode(cert_pem)
base64_key_pem = base64.b64encode(key_pem)

with open("./cert.d/base64_ingress_controller.crt", "wb") as f:
    f.write(base64_cert_pem)

with open("./cert.d/base64_ingress_controller.key", "wb") as f:
    f.write(base64_key_pem)