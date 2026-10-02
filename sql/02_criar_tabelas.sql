-- Script para criação dos schemas

create schema if not exists raw;

create schema if not exists processed;


-- Script para a criação das tabelas

CREATE TABLE raw.supermarket_sales (
    invoice_id VARCHAR(20) PRIMARY KEY,
    branch VARCHAR(5),
    city VARCHAR(50),
    customer_type VARCHAR(20),
    gender VARCHAR(10),
    product_line VARCHAR(50),
    unit_price NUMERIC(10,2),
    quantity INTEGER,
    tax_5_percent NUMERIC(10,4),
    total NUMERIC(10,4),
    data_venda VARCHAR(15),
    time TIME,
    payment VARCHAR(20),
    cogs NUMERIC(10,4),
    gross_margin_percentage NUMERIC(10,6),
    gross_income NUMERIC(10,4),
    rating NUMERIC(3,1)
);


create table if not exists processed.vendas_tratadas (
    id_venda varchar(50) primary key not null,
    filial varchar(10) not null,
    cidade varchar(100) not null,
    tipo_cliente varchar(50),
    genero varchar(20),
    linha_produto varchar(150) not null,
    preco_unitario numeric(10, 2) check (preco_unitario >= 0),
    quantidade integer check (quantidade > 0),
    imposto numeric(10, 2) check (imposto >= 0),
    valor_total numeric(12, 2) check (valor_total >= 0),
    data_venda date,
    hora_venda time,
    forma_pagamento varchar(50) not null,
    custo_mercadoria numeric(12, 2) check (custo_mercadoria >= 0),
    margem_percentual numeric(10, 2),
    receita_bruta numeric(12, 2) check (receita_bruta >= 0),
    avaliacao numeric(4, 2) check (avaliacao between 0 and 10)
);