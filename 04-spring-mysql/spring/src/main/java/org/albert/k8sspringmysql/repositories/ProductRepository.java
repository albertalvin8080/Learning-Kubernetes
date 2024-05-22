package org.albert.k8sspringmysql.repositories;

import org.albert.k8sspringmysql.domain.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {

}
