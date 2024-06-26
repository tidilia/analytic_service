import React, { useState } from 'react'
import { Container, Spinner } from 'react-bootstrap';
import { useRef, useEffect } from 'react';
import ProductsListGroup from './ProductsListGroup';
import axios, { CanceledError } from 'axios'
import Card from 'react-bootstrap/Card';

interface seoProduct {
  nmID: number,
  description: string
}


function SEOComponent() {
  const [resultValue, setResultValue] = useState("Описание")
  const [isProduct, setIsProduct] = useState(false)
  const [loading, setLoading] = useState(false)
  const [info, setInfo] = useState<seoProduct>({
    nmID: -1,
    description: ""
  });
  const endpoint = `${import.meta.env.VITE_API_URL}seo/create/`

  const inputContainerStyle = {
    // display: 'flex',
    // flexDirection: 'column' as 'column',
    // alignItems: 'center',
    marginTop: '20px',
  };

  const handleSelectItem = (item: any) => {
    setIsProduct(true)
    setInfo({ ...info, nmID: item.nmID })
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(info)
  }


  const sendData = async (e) => {
    if (info.nmID != -1) {
      e.preventDefault();
      setLoading(true);
      const controller = new AbortController();
      console.log(info)

      const response = await axios
        .post<string>(endpoint, info, { signal: controller.signal })
        .then(res => {
          setResultValue(res.data)
          setLoading(false)
        }
        )
        .catch(err => {
          setLoading(false);
          if (err instanceof CanceledError) return;
          console.log(err.message)
        }
        );

      console.log(response)

      return () => controller.abort()
    } else {
      setIsProduct(false)
    }
  }

  return (
    <>
      <ProductsListGroup
        heading="Выберите товар для SEO-оптимизации"
        onSelectItem={handleSelectItem}
        listType="part" 
        loading={loading}/>
      <Container>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="features" className="form-label">Особенности</label>
            <textarea
              onChange={(event) =>
                setInfo({ ...info, description: event.target.value })
              }
              value={info.description}
              id="features"
              className="form-control"
              rows={4}
              disabled={loading} />
          </div>
          {!isProduct && <p style={{ color: 'red' }}>Выберите товар!</p>}
          <button
            className="btn btn-primary"
            type="submit"
            onClick={sendData}
            disabled={loading}
          >{loading ? (
            <Spinner animation="border" size="sm" role="status" />
          ) : (
            'Получить описание'
          )}</button>
        </form>
        <div style={inputContainerStyle}>
          <Card body data-bs-theme="dark">{resultValue}</Card>
        </div>
      </Container>
    </>
  );
}

export default SEOComponent;