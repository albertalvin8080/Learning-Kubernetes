package org.albert.hashcorptest;

import org.albert.hashcorptest.config.VaultConfig;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@SpringBootApplication
@RequiredArgsConstructor
@EnableConfigurationProperties(value = VaultConfig.class)
public class HashcorptestApplication implements CommandLineRunner
{
    private final VaultConfig vaultConfig;

    public static void main(String[] args) {
        SpringApplication.run(HashcorptestApplication.class, args);
    }

    // mvn clean install -DskipTests
    // java -jar target/spring-hashcorp-test-0.0.1-SNAPSHOT.jar
    // java -jar target/spring-hashcorp-test-0.0.1-SNAPSHOT.jar trebla 4321
    @Override
    public void run(String... args) throws Exception {
        if (args.length >= 2) {
            log.info("Username: {}", args[0]);
            log.info("Password: {}", args[1]);
        }
        else {
            log.info("Vault Username: {}", vaultConfig.getUsername());
            log.info("Vault Password: {}", vaultConfig.getPassword());
        }
    }

}
