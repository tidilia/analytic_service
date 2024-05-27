import React, { useState } from 'react'
import { Container } from 'react-bootstrap';
import { useRef, useEffect } from 'react';
import ProductsListGroup from './ProductsListGroup';
import axios, { CanceledError } from 'axios'

interface seoProduct {
  nmID: number,
  amount: number,
  description: string
}

function SEOComponent() {
  const [info, setInfo] = useState<seoProduct>({
    nmID: -1,
    amount: 0,
    description: ""
  });
  const amountRef = useRef<HTMLInputElement>(null)
  const endpoint = `${import.meta.env.VITE_API_URL}seo/create/`


  const handleSelectItem = (item: any) => {
    setInfo({ ...info, nmID: item.nmID, amount: item.quantity })
    if (amountRef.current?.value || amountRef.current?.value === "") {
      amountRef.current.value = (item.quantity)
    }
  }

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log(info)
  }

  const sendData = async () => {
    const controller = new AbortController();
    console.log(info)

    const response = await axios
      .post(endpoint, info, { signal: controller.signal })
      .then(res => console.log(res))
      .catch(err => {
        if (err instanceof CanceledError) return;
        console.log(err.message)
      }
      );

    console.log(response)

    return () => controller.abort()
  }

  return (
    <>
      <ProductsListGroup heading="Выберите товар для SEO-оптимизации" onSelectItem={handleSelectItem} listType="part" />
      <Container>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="amount" className="form-label">Количество</label>
            <input onChange={(event) =>
              setInfo({ ...info, amount: parseInt(event.target.value) })
            }
              value={info.amount}
              id="amount"
              type="number"
              className="form-control"
              ref={amountRef} />
          </div>
          <div className="mb-3">
            <label htmlFor="features" className="form-label">Особенности</label>
            <textarea onChange={(event) =>
              setInfo({ ...info, description: event.target.value })
            }
              value={info.description}
              id="features"
              className="form-control"
              rows={4} />
          </div>
          <button className="btn btn-primary" type="submit" onClick={sendData}>Получить описание</button>
        </form>
      </Container>
    </>
  );
}

export default SEOComponent;