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

📦 Instalación de Dependencias

Instala las dependencias del proyecto:

```npm install```

2. **Instala Newman y el reportero HTML de forma global:**

```npm install -g newman newman-reporter-htmlextra```

## 🚀 Ejecución del Servidor

```npm start```

Una vez levantado, la consola indicará que los servicios están activos. El servidor expone los siguientes puntos de entrada:

Base URL: http://localhost:4000

Endpoint REST (Users): http://localhost:4000/api/v1/users

Endpoint GraphQL: http://localhost:4000/graphql




## 🧪 Suite de Pruebas y Cobertura
## Ejecución de Pruebas con Newman
## Pruebas Basadas en Datos (DDT)
## Generación de Reportes HTML

