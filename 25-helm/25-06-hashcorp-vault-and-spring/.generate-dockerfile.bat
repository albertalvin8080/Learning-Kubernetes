@echo off
setlocal

cd spring-hashcorp-test

call mvn clean install -DskipTests

call docker build -t albertalvin/spring-hashcorp-test:1.0.3-eclipse-temurin .

call docker push albertalvin/spring-hashcorp-test:1.0.3-eclipse-temurin

endlocal

@REM docker run --name spring -e SPRING_PROFILES_ACTIVE=kubernetes albertalvin/spring-hashcorp-test:1.0.0-eclipse-temurin