# Barter - Plataforma de Trueques

**Equipo de Desarrollo - Diseño de Software II**  



---

## Descripción
Barter es una plataforma e-commerce especializada en trueques, que permite a los usuarios intercambiar productos o servicios sin utilizar dinero como medio de pago. El proyecto está desarrollado usando una arquitectura de microservicios basada en **Clean Architecture**, con tecnologías modernas que garantizan **escalabilidad, mantenibilidad y facilidad de integración**.

---

## Características Principales
- Registro y autenticación de usuarios con correo electrónico o redes sociales.
- Publicación y gestión de ofertas de trueque con imágenes y descripciones.
- Búsqueda y filtrado de ofertas por categoría, ubicación y palabras clave.
- Negociación entre usuarios mediante chat y propuestas de intercambio.
- Notificaciones en tiempo real sobre estado de trueques y mensajes.
- Valoración y reputación de usuarios tras concretar un trueque.
- Panel de administración básico para supervisar la plataforma.

---

## Tecnologías Utilizadas
- **Frontend:** React
- **Backend:** NestJS (Node.js + TypeScript)
- **Base de datos:** PostgreSQL
- **Mensajería:** Kafka o RabbitMQ para comunicación asíncrona y eventos
- **Documentación API:** Swagger / OpenAPI
- **Contenerización:** Docker, docker-compose
- **Orquestación:** Kubernetes (Minikube)
- **Arquitectura:** Clean Architecture

---

## Estructura del Proyecto
El repositorio contiene la estructura inicial basada en microservicios con carpetas organizadas por capas, integrando:

- Microservicios independientes con sus propias bases de datos.
- Esqueleto de los servicios con contratos y documentación OpenAPI.
- Configuración para el ambiente local con `docker-compose.dev.yml`.
- Scripts para pruebas unitarias y generación de reportes.
- Manifiestos básicos para despliegue en Kubernetes.
- Configuración inicial para Service Mesh con Istio o Linkerd.

---

## Instalación y Ejecución Local

1. Clonar el repositorio y levantar la BD:

```bash
git clone <repo-url>
cd barter
docker-compose -f docker-compose.dev.yml up -d
