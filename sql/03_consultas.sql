-- Calcular a quantidade de vendas por filial
SELECT 
	filial, 
	count(*) AS total_vendas
FROM raw.raw_vendas rv 
GROUP BY filial
ORDER BY 2 desc;


-- Calcular o total de vendas por linha de produto
SELECT 
	linha_produto , 
	count(*) AS total_vendas
FROM raw.raw_vendas rv 
GROUP BY linha_produto
ORDER BY 2 desc;


-- Calcular o total de vendas por ano
SELECT 
	date_part('year', to_date(data_venda, 'MM/DD/YYYY'))::int AS ano,
	count(*)
FROM raw.raw_vendas
GROUP BY 1;


-- total de itens vendidos por categoria
SELECT 
	linha_produto,
	sum(quantidade) AS total_itens_vendidos
FROM raw.raw_vendas rv 
GROUP BY 1
ORDER BY 2 DESC;


-- Média do cuto da mercadoria por linha de produto
SELECT 
	linha_produto,
	round(avg(custo_mercadoria)::numeric,2) AS custo_medio
FROM raw.raw_vendas rv 
GROUP BY 1
ORDER BY 2 DESC;


-- Média das avaliações por filial
SELECT 
	filial,
	round(avg(avaliacao)::numeric, 2) AS media_avaliacoes
FROM raw.raw_vendas rv 
GROUP BY 1
ORDER BY 2 desc;


-- Média de vendas por forma de pagamento
SELECT 
	forma_pagamento,
	round(avg(valor_total)::NUMERIC,2) AS media_valor_total
FROM raw.raw_vendas rv 
GROUP BY 1
ORDER BY 2 DESC;