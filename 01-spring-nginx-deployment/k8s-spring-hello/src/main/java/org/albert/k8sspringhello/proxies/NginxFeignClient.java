package org.albert.k8sspringhello.proxies;

import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

@FeignClient(name = "nginxFeignClient", url = "${nginx.url}")
public interface NginxFeignClient {
    @GetMapping(produces = MediaType.TEXT_HTML_VALUE)
    ResponseEntity<String> getNginxHello();
}
