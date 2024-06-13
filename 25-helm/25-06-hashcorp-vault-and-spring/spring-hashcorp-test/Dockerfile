FROM eclipse-temurin:17.0.11_9-jre-jammy

LABEL authors="Albert"

VOLUME /tmp

WORKDIR /app

COPY /target/spring-hashcorp-test-0.0.1-SNAPSHOT.jar app.jar

CMD ["java", "-jar", "app.jar"]