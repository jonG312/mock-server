![Node.js](https://img.shields.io/badge/Node.js-18%2B-green)
![Postman](https://img.shields.io/badge/Postman-Testing-orange)
![Newman](https://img.shields.io/badge/Newman-Automated%20Testing-blue)
![GraphQL](https://img.shields.io/badge/GraphQL-API-E10098)

# 🚀 Mock Server API & Automated Testing Suite

Servidor Mock desarrollado con Node.js y Express para emular endpoints REST y GraphQL, acompañado de una suite de pruebas automatizadas en Postman ejecutadas mediante **Newman** con soporte para **Data-Driven Testing (DDT)** y **reportes gráficos en HTML**.

---

## 📋 Tabla de Contenidos
- [Características del Proyecto](#-características-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Ejecución del Servidor](#-ejecución-del-servidor)
- [Suite de Pruebas y Cobertura](#-suite-de-pruebas-y-cobertura)
- [Ejecución de Pruebas con Newman](#-ejecución-de-pruebas-con-newman)
- [Pruebas Basadas en Datos (DDT)](#-pruebas-basadas-en-datos-ddt)
- [Generación de Reportes HTML](#-generación-de-reportes-html)

---

## 🎯 Características del Proyecto
* **API REST & GraphQL Mock:** Simulación de endpoints para testing de integración y rendimiento.
* **Validación de Respuestas:** Cobertura de códigos de estado HTTP (200, 500) y tiempos de respuesta (< 500ms).
* **Pruebas Basadas en Datos (DDT):** Ejecución iterativa utilizando un conjunto de datos dinámico (`data.json`).
* **Reportes Visuales:** Generación automática de dashboards interactivos mediante `htmlextra`.

---

## 🛠️ Requisitos Previos
Asegúrate de contar con los siguientes elementos instalados en tu sistema:

* [Node.js](https://nodejs.org/) (Versión 18 o superior)
* [npm](https://www.npmjs.com/) (Incluido con Node.js)
* [Postman](https://www.postman.com/) (Opcional, para exploración de endpoints)

---

## 📦 Instalación y Configuración

1. **Clona el repositorio o navega a la carpeta del proyecto:**

   ```cd mock-server```

2. Instalación de Dependencias

Instala las dependencias del proyecto:

```npm install```

3. **Instala Newman y el reportero HTML de forma global:**

```npm install -g newman newman-reporter-htmlextra```

## 🚀 Ejecución del Servidor

```npm start```

Una vez levantado, la consola indicará que los servicios están activos. El servidor expone los siguientes puntos de entrada:

Base URL: http://localhost:4000

Endpoint REST (Users): http://localhost:4000/api/v1/users

Endpoint GraphQL: http://localhost:4000/graphql




## 🧪 Suite de Pruebas y Cobertura

La colección de Postman se encuentra en:

```postman/api_health_checks.json```

1. **Endpoint REST**

Método:

```GET /api/v1/users```

Las pruebas verifican:

Status Code Check: El código de respuesta HTTP debe ser 200 OK.
Latency Check: El tiempo de respuesta debe ser inferior a 500 ms.

2. Endpoint GraphQL

Método:

```POST /graphql```

Las pruebas verifican:

Schema & Query Validation: Ejecuta una consulta checkService solicitando los campos:
- service
- healthy
- latencyMs
- Error Prevention: Verifica que la respuesta JSON no contenga la propiedad "errors".


## ⚙️ Ejecución de Pruebas con Newman

Newman te permite correr la suite directamente en la consola sin necesidad de abrir la interfaz gráfica de Postman.

Para lanzar una ejecución simple de la colección:

```newman run postman/api_health_checks.json```

## 📊 Pruebas Basadas en Datos (DDT - Data-Driven Testing)

El proyecto soporta pruebas basadas en datos externos mediante el archivo:

```data.json```

Esto permite ejecutar múltiples iteraciones utilizando diferentes registros de datos.

Para ejecutar la colección utilizando el dataset:

```newman run postman/api_health_checks.json -d data.json```

durante la ejecución Newman:

   - Detecta la cantidad de registros disponibles en data.json.
   - Ejecuta una iteración de la suite por cada registro.
   - Sustituye dinámicamente las variables:
      ```{{name}}```
      ```{{email}}```
      ```{{role}}```
   - Muestra un resumen de las aserciones exitosas y fallidas de cada iteración.

## 📄 Generación de Reportes HTML

Para generar un reporte HTML visual e interactivo:

```newman run postman/api_health_checks.json -d data.json -r htmlextra```

El reporte generado estará disponible en la carpeta:

```/newman```

Características del reporte
   - Dashboard visual: Muestra el porcentaje total de pruebas exitosas y fallidas.
   - Tiempo de respuesta: Permite analizar el tiempo medio de respuesta.
   - Detalle por iteración: Muestra información individual de cada ejecución.
   - Logs HTTP completos: Permite inspeccionar:
   - Headers de la petición.
   - Request Body.
   - Response Body.
   - Errores HTTP.
   - Fallos de aserciones.

Esto facilita la depuración de errores como respuestas 500 o fallos en las validaciones automatizadas.

## 📁 Estructura del Proyecto

.
├── postman/
│   └── api_health_checks.json
├── data.json
├── newman/
│   └── *.html
├── package.json
└── README.md

## 🛠️ Tecnologías Utilizadas

- Node.js
- Postman
- Newman
- Newman HTML Extra Reporter
- REST API
- GraphQL
- Data-Driven Testing (DDT)
- Automated Integration Testing
