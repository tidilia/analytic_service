import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';


function NavigationBar() {
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/">Сервис аналитики</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/products">Товары</Nav.Link>
            <Nav.Link href="/seo">СЕО</Nav.Link>
            <Nav.Link href="/reports">Отчеты</Nav.Link>
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default NavigationBar;