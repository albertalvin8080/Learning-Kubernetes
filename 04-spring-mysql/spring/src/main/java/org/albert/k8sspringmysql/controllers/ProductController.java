package org.albert.k8sspringmysql.controllers;

import java.util.List;

import org.albert.k8sspringmysql.domain.Product;
import org.albert.k8sspringmysql.services.ProductService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
public class ProductController 
{
    private final ProductService service;

    @GetMapping(path = "/all")
    public ResponseEntity<List<Product>> findAll() 
    {
        return ResponseEntity.ok(service.findAll());
    }

    @PostMapping(path = "/save")
    public ResponseEntity<Product> save(@RequestBody Product product) {
        return ResponseEntity.ok(service.save(product));
    }
}
