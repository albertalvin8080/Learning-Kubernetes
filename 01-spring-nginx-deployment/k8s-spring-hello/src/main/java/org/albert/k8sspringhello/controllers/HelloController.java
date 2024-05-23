package org.albert.k8sspringhello.controllers;

import java.net.InetAddress;
import java.net.UnknownHostException;

import org.albert.k8sspringhello.proxies.NginxFeignClient;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
public class HelloController {
    private final NginxFeignClient nginxFeignClient;

    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> hello(HttpServletRequest httpRequest) throws UnknownHostException {
        final String hostname = InetAddress.getLocalHost().getHostName();
        final String requestURL = httpRequest.getRequestURL().toString();
        final String remoteHost = httpRequest.getRemoteHost();

        final String json = String.format("""
                {
                    "hostname":"%s", "requestURL":"%s", "remoteHost":"%s"
                }
                """,
                hostname, requestURL, remoteHost)
                .replaceAll("((?<!\\b+)\\s+)|(\\s+(?!\\b+))", "");

        return ResponseEntity.ok(json);
    }

    @GetMapping(path = "/nginx", produces = MediaType.TEXT_HTML_VALUE)
    public ResponseEntity<String> nginxHello() {
        // return ResponseEntity.ok(nginxFeignClient.getNginxHello().getBody());
        return nginxFeignClient.getNginxHello();
    }
}
