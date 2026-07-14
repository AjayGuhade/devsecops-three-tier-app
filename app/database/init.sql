-- =====================================================
-- DevSecOps Three-Tier Application
-- Database Initialization Script
-- Sprint 2 - Docker & Containerization
-- =====================================================

-- Create database
CREATE DATABASE IF NOT EXISTS employee_db;

-- Select database
USE employee_db;

-- Create employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample employee records
INSERT INTO employees (name, department, email)
VALUES
('Ajay Guhade', 'DevOps', 'ajay@example.com'),
('John Doe', 'Engineering', 'john.doe@example.com'),
('Jane Smith', 'Human Resources', 'jane.smith@example.com');