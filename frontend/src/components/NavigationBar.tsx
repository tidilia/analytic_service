import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


function NavigationBar() {
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="#home">Сервис аналитики</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="">Товары</Nav.Link>
            <Nav.Link href="#Seo">СЕО</Nav.Link>
            <Nav.Link href="#pricing">Отчеты</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default NavigationBar;