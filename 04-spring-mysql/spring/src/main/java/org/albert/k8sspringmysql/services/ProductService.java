package org.albert.k8sspringmysql.services;

import java.util.List;

import org.albert.k8sspringmysql.domain.Product;
import org.albert.k8sspringmysql.repositories.ProductRepository;
import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ProductService {
    private final ProductRepository repository;

    public List<Product> findAll() {
        return repository.findAll();
    }

    public Product save(final Product product) {
        return repository.save(product);
    }
}
