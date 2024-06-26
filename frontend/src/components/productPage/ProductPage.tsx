import axios, { CanceledError } from 'axios';
import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ChartComponent from './ChartComponent';
import PieChartComponent from './PieChartComponent';
import Image from 'react-bootstrap/Image';
import BarChartComponent from './BarChartComponent';
import { Container, Row, Col } from 'react-bootstrap';
import IndicatorsTableComponent from './IndicatorsTableComponent';
import ProfitCounterComponent from './ProfitCounterComponent';

interface InfoI {
    nmID: number
}

interface OrderI {
    nmID: number,
    sku: string,
    date: Date,
    time: number,
    size: string
}

interface ConversionsI {
    cancelCount: number,
    buyoutsCount: number
    openCardCount: number,
    addToCartCount: number,
    ordersCount: number,
    ordersSumRub: number,
    buyoutsSumRub: number,
    cancelSumRub: number,
    avgPriceRub: number
}
type DataPoint = {
    name: number | string;
    value: number;
};

interface mainInfoI {
    name: string,
    nmID: number,
    photo: string,
    sizes: string
}

interface Dictionary {
    [key: string]: number;
}

const ProductPage: React.FC = (): JSX.Element => {
    const endpoint = `${import.meta.env.VITE_API_URL}productItemData/`
    const endpoint_main_info = `${import.meta.env.VITE_API_URL}getProduct/`
    const params = useParams();
    const info: InfoI = { nmID: Number(params.id) }
    const [dayOrders, setDayOrders] = useState<OrderI[]>([])
    const [weekOrders, setWeekOrders] = useState<OrderI[]>([])
    const [error, setError] = useState("")
    const [mainInfo, setMainInfo] = useState<mainInfoI>({
        name: "",
        nmID: 0,
        photo: "",
        sizes: ""
    })
    const [conversionsData, setConversionsData] = useState<ConversionsI>({
        buyoutsCount: 0,
        cancelCount: 0,
        openCardCount: 0,
        addToCartCount: 0,
        ordersCount: 0,
        ordersSumRub: 0,
        buyoutsSumRub: 0,
        cancelSumRub: 0,
        avgPriceRub: 0
    })
    const inputContainerStyle = {
        display: 'flex',
        flexDirection: 'column' as 'column',
        alignItems: 'center',
        marginTop: '20px',
    };

    const getSizeOrders = (rowOrdersData: OrderI[]) => {
        var sizeOrders: Dictionary = {}
        var sizes = mainInfo.sizes.split(", ")
        var result: DataPoint[] = []

        sizes.map(val =>
            sizeOrders[val] = 0
        )

        rowOrdersData.map(order => {
            console.log(order.size)
            sizeOrders[order.size] += 1
        })

        sizes.map(val =>
            result.push({ name: val, value: sizeOrders[val] })
        )
        return result
    }

    const getOrdersData = (rowOrdersData: OrderI[], ordersType: "day" | "week") => {
        var ordersData: DataPoint[] = []
        const n = (ordersType == "day") ? 24 : 7
        var ordersTimes: number[] = new Array(n)
        const days: string[] = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

        for (var i = 0; i < ordersTimes.length; i++) {
            ordersTimes[i] = 0;
        }

        rowOrdersData?.map((order) => {
            ordersTimes[order.time] += 1

        })

        ordersTimes.map((orders_n, index) => {
            var i = (ordersType == "week") ? (days[index]) : index
            var newItem: DataPoint = {
                name: i,
                value: orders_n
            }
            ordersData.push(newItem)
        })

        return ordersData
    }

    useEffect(() => {
        const controller = new AbortController();

        axios
            .post<OrderI[]>(endpoint + 'getDayOrders/', info, { signal: controller.signal })
            .then(res =>
                setDayOrders(res.data))
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()
    }, [])

    useEffect(() => {
        const controller = new AbortController();

        axios
            .post<OrderI[]>(endpoint + 'getWeekOrders/', info, { signal: controller.signal })
            .then(res => {
                setWeekOrders(res.data)
            })
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()
    }, [])

    useEffect(() => {
        const controller = new AbortController();

        axios
            .post<mainInfoI[]>(endpoint_main_info, info, { signal: controller.signal })
            .then(res => {
                res.data.map((r) =>
                    setMainInfo(r)
                )
            })
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()
    }, [])

    useEffect(() => {
        const controller = new AbortController();

        axios
            .post<ConversionsI>(endpoint + 'getConversions/', info, { signal: controller.signal })
            .then(res => {
                setConversionsData(res.data)
            })
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()
    }, [])


    return (
        <>
            <div style={{ display: "flex" }}>
                <div style={{ margin: '10px 50px 0px 20px' }}>
                    <Image
                        src={mainInfo.photo} rounded
                        width={78}
                        height={104}
                    />
                </div>
                <div style={{ margin: '25px 0px 0px 0px' }}>
                    <h1>{mainInfo.name}</h1>
                </div>
            </div>
            <Container >
                <Row>
                    <Col>
                        <IndicatorsTableComponent data={conversionsData} heading='Общие данные за месяц'/>
                    </Col>
                    <Col>
                        <ProfitCounterComponent info={info} heading='Рассчитать прибыль за месяц'/>
                    </Col>
                </Row>
            </Container>
            <table className='table'>
                <tr>
                    <td> <ChartComponent
                        data={getOrdersData(dayOrders, "day")}
                        chartType='day'
                        heading='Заказы за день'>
                    </ChartComponent> </td>
                    <td><ChartComponent
                        data={getOrdersData(weekOrders, "week")}
                        chartType='week'
                        heading='Заказы за неделю'>
                    </ChartComponent></td>
                </tr>
            </table>
            <Container style={inputContainerStyle}>
                <Row>
                    <Col>
                        <BarChartComponent
                            data={getSizeOrders(weekOrders)}
                            heading='Заказы за неделю по размерам' />
                    </Col>
                </Row>
            </Container>
            <div style={{ textAlign: 'center' }}>
                <h2>Показатели конверсии за последний месяц</h2>
            </div>
            <table className='table'>
                <tr>
                    <td>
                        <PieChartComponent data={[
                            {
                                name: "выкупили",
                                value: conversionsData.buyoutsCount
                            },
                            {
                                name: "отказались",
                                value: conversionsData.cancelCount
                            }]} /></td>
                    <td><PieChartComponent data={[
                        {
                            name: "положившие в корзину",
                            value: conversionsData.addToCartCount
                        },
                        {
                            name: "другие открывшие карточку товара",
                            value: conversionsData.openCardCount - conversionsData.addToCartCount
                        }]} /></td>
                    <td><PieChartComponent data={[
                        {
                            name: "сделавшие заказ",
                            value: conversionsData.ordersCount
                        }, {
                            name: "другие открывшие карточку товара",
                            value: conversionsData.openCardCount - conversionsData.ordersCount
                        }]} /></td>
                </tr>
            </table>
        </>
    )
}

export default ProductPage