import React from 'react';
import { Container, Row, Col, Image } from 'react-bootstrap';
import mainPhoto from "./mainPhoto.webp"

const HomePage = () => {
    const description = "Интеллектуальная аналитика на маркетплейсе: получайте ценные данные, прогнозируйте тренды и принимайте обоснованные решения для вашего бизнеса."
    const information = " Наш сервис аналитики на маркетплейсе предоставляет мощные инструменты для проведения глубокого анализа данных. Получайте ценные исследовательские выводы, определяйте ключевые тренды и паттерны, а также прогнозируйте результаты на основе точных данных. Улучшайте эффективность вашего бизнеса, принимая обоснованные решения на основе аналитики. Присоединяйтесь к нам сегодня и начните использовать возможности нашего сервиса для достижения успеха на маркетплейсе."
    return (
        <Container fluid>
            <Row>
                <Col xs={12} md={6}>
                    <Image src={mainPhoto}
                        alt="Image" fluid />
                </Col>
                <Col xs={12} md={6} className="d-flex align-items-center">
                    <div>
                        <h1 className="mb-4">Сервис аналитики</h1>
                        <h3 className="mb-4">{description}</h3>
                        <p className="text-muted">{information}</p>
                    </div>
                </Col>
            </Row>
        </Container>);
};
export default HomePage;