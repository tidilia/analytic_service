import { useState, useEffect, useRef } from 'react'
import axios, { CanceledError } from 'axios'
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';
import { useTransition } from 'react';

interface Product {
    nmID: number,
    name: string,
    photo: string,
    quantity: number,
    price: string,
    sizes: string
}

interface Props {
    heading: string;
    onSelectItem: (item: Product) => void;
    listType: "full" | "part";
    loading: boolean
}

interface Dictionary {
    [key: string]: string;
}

function ProductsListGroup({ heading, onSelectItem, listType, loading }: Props) {
    const [productsData, setProductsData] = useState<Product[]>([])
    const [selectedIndex, setSelectedIndex] = useState(-1)
    const [_, startTransition] = useTransition()
    const [filter, setFilter] = useState("")
    const [error, setError] = useState("")
    const inputProductRef = useRef<HTMLInputElement>(null)
    const endpoint = `${import.meta.env.VITE_API_URL}products/`
    const isPart = (listType == "part") ? true : false
    type productAccessors = Array<keyof Product>

    var atr: Dictionary = {}
    var w: number, h: number
    var containerID: string = ""
    const f: Dictionary = { "quantity": "Количество", "sizes": "Размеры", "price": "Цена" };
    const p: Dictionary = { "name": "Наименование товара", "nmID": "Артикул WB" }

    const changeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
        startTransition(() => {
            setFilter(event.target.value)
        })
    }

    const selectHandler = (el: Product) => {
        if (inputProductRef.current?.value || inputProductRef.current?.value === "")
            inputProductRef.current.value = el.name
        setFilter("")
    }

    useEffect(() => {
        const controller = new AbortController();

        axios
            .get<Product[]>(endpoint, { signal: controller.signal })
            .then(res => setProductsData(res.data))
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()
    }, [])

    const filterItems = (filter: string) => {
        var l: Product[] = []
        if (listType === "full")
            l = productsData
        return filter
            ? productsData.filter(i =>
            (i.name.toLowerCase().includes(filter.toLowerCase())
                || i.nmID.toString().includes(filter.toLowerCase()))
            )
            : l
    }

    if (listType === "full") {
        atr = f
        w = 78
        h = 104
    } else if (listType === "part") {
        atr = p
        w = 30
        h = 40
    }
    containerID = listType + "Container"
    const items = filterItems(filter)


    return (
        <>
            {!isPart && <p className="fs-5">{heading}</p>}
            {error && <p className='text-danger'>{error}</p>}
            {productsData.length === 0 && <p>Товары не найдены.</p>}
            <Container>
                {isPart && <label htmlFor="productInput" className="form-label">Выберите товар для SEO-оптимизации</label>}
                <input
                    className='form-control'
                    ref={inputProductRef}
                    type="text"
                    onChange={changeHandler}
                    id='productInput' 
                    disabled={loading}/>
                <ul className="list-group" id={containerID}>
                    {!isPart && <>
                        <li className='list-group-item' key={0}>
                            <Container>
                                <Row>
                                    <Col>
                                        <>Фото</>
                                    </Col>
                                    <Col>
                                        <>Наименование товара</>
                                    </Col>
                                    {(Object.keys(atr) as productAccessors).map((atrib) =>
                                        <Col>
                                            <>{atr[atrib]}</>
                                        </Col>
                                    )}
                                </Row>
                            </Container>
                        </li>
                    </>}
                    {items.map((el, index) =>
                        <li
                            key={el.nmID}
                            className={selectedIndex === index ? 'list-group-item active' : 'list-group-item'}
                            onClick={() => {
                                setSelectedIndex(index);
                                selectHandler(el);
                                onSelectItem(el);
                            }}
                        >
                            <Container>
                                <Row>
                                    <Col>
                                        <Image
                                            src={el.photo} rounded
                                            width={w}
                                            height={h} />
                                    </Col>
                                    {!isPart && <Col>
                                        <a href={'http://localhost:5173/products/' + el.nmID.toString()} onClick={() => { onSelectItem(el) }}>{el.name}</a>
                                    </Col>}
                                    {(Object.keys(atr) as productAccessors).map((atrib) =>
                                        <Col>
                                            <>{el[atrib]}</>
                                        </Col>
                                    )}
                                </Row>
                            </Container>
                        </li>
                    )}
                </ul>
            </Container >
        </>
    );
}

export default ProductsListGroup;