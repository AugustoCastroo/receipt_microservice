# Ingeniería de Software - Proyecto

## 📚 Información de la Materia
- **Asignatura:** Ingeniería de Software  
- **Curso:** 4º Año  
- **Carrera:** Ingeniería en Informática  
- **Profesor Titular:** Lic. Pablo Andrés Prats  

---

# Receipt-Microservices

## 📝 Descripción del Microservicio de Receipts

Este microservicio gestiona los comprobantes (receipts) de la aplicación. Permite registrar, consultar y actualizar información relacionada con los recibos, sus encabezados, pies, ítems y tipos. Se encarga de orquestar la creación de comprobantes, asociar artículos y lotes a cada recibo, y mantener la integridad de los datos relacionados con las operaciones de ingreso y egreso de inventario.

Entre sus funcionalidades principales se encuentran:

- Registrar nuevos recibos con sus ítems, encabezados y pies.
- Consultar recibos individuales o listarlos todos.
- Asociar artículos y lotes a los ítems de cada recibo.
- Integrarse con otros microservicios (Stock, Article, Batch) para mantener la coherencia de la información.
- Gestionar los tipos de recibos y sus efectos sobre el stock.

---

## 🛠️ Tareas del Proyecto

### Gestión del Proyecto
- Redacción de historias de usuario.
- Planificación y ejecución de Sprints a través de GitHub Projects.

### Diseño y Arquitectura
- Implementación de diagramas de clases y secuencia (carpeta docs).
- Aplicación de arquitectura de microservicios.
- Patrones de microservicios aplicados:
  - API Gateway
  - Strangler
  - Decompose by Business Capability
  - Resiliencia (Bulkhead, Circuit Breaker, Cache de Objetos)
- Diseño de APIs REST para comunicación entre servicios.

### Desarrollo y Despliegue
- Creación y despliegue de contenedores Docker.
  - Dockerfile
  - docker-compose.yml
  - Para construir: `docker build -t microservice-receipt:TAG .`
  - Para crear red: `docker network create mired`
  - Para ejecutar: `docker compose up -d`
- Implementación de servicios independientes (PostgreSQL) mediante contenedores.
- Aplicación de patrones de diseño.
- Uso de Git con flujos de trabajo Trunk-based Development.
- Versionado adecuado del código.
- Metodologías ágiles utilizando Scrum a través de GitHub Projects.
- Contenedor para servicios y para el proyecto con Docker (carpeta docker).

---

## Variables de entorno:
```
URL_ARTICLE_SERVICE=https://article.universidad.localhost/api/v1
URL_STOCK_SERVICE=https://article.universidad.localhost/api/v1
```

---

## Patrones de microservicios aplicados:

- Patron Saga
- Bulkhead
- Circuit Breaker
- Service Layer
- Repository
- DTO (Data Transfer Object)
- Mapper/Schema (Marshmallow)
- Retry (Tenacity)
- MVC (Model-View-Controller)
- API Gateway (integración)
- Decompose by Business Capability
- Resiliencia

Más información:
- https://microservices.io/patterns/data/saga.html
- https://microservices.io/patterns/reliability/circuit-breaker.html

---

## 🏗️ Estructura del Proyecto

receipt_microservice/
├── docs/
│   └── (diagramas)
├── app/
│   ├── models/
│   ├── controllers/
│   ├── mapping/
│   ├── services/
│   ├── repositories/
│   └── dto/
├── docker/
│   ├── db/
│   │   ├── data/
│   │   └── docker-compose.yml
│   └── app/
│       └── docker-compose.yml
├── test/
├── README.md
└── Dockerfile

---

## 🔧 Tecnologías Utilizadas

- **Lenguaje:** Python
- **Framework:** Flask
- **Arquitectura:** Microservicio Receipt - Aplicación Cliente Servidor (Backend)
- **Control de Versiones:** Git
- **Comunicación:** APIs REST/JSON
- **Principios y Patrones:** YAGNI, SOLID, DRY, MVC, Repository, Service Layer, DTO, Mapper, Retry

---

## 👥 Equipo de Desarrollo

- Jose Ruti
- Augusto Castro