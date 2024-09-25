-- Criar a tabela 'pessoa'
CREATE TABLE person (
    id SERIAL PRIMARY KEY,  -- ID como chave primária
    cpf VARCHAR(11) NOT NULL UNIQUE,  -- CPF como campo único
    name VARCHAR(100) NOT NULL,
    age INT,
    cnh VARCHAR(20)
);

-- Criar a tabela 'carro'
CREATE TABLE car (
    id SERIAL PRIMARY KEY,  -- ID como chave primária
    plate VARCHAR(10) NOT NULL UNIQUE,  -- Placa como campo único
    model VARCHAR(100) NOT NULL,
    year INT
);

-- Criar a tabela 'motorista'
CREATE TABLE driver (
    id SERIAL PRIMARY KEY,  -- ID como chave primária
    person_id INT REFERENCES person(id),  -- Referenciando o ID da tabela pessoa
    car_id INT REFERENCES car(id)  -- Referenciando o ID da tabela carro
);

---- Inserindo pessoas
INSERT INTO person (cpf, name, age, cnh) VALUES
('46787766050', 'John', 30, '73042428608'),
('52251251073', 'Maria', 25, '24388792534');

-- Inserindo carros
INSERT INTO car (plate, model, year) VALUES
('ITN6029', 'Honda Civic', 2015),
('MQB2875', 'Ford Focus', 2018);

-- Associando motoristas a carros usando IDs
INSERT INTO driver (person_id, car_id) VALUES
(1, 1),  -- Associando John ao Honda Civic
(2, 2);  -- Associando Maria ao Ford Focus
