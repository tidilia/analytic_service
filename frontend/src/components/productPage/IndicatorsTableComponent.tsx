import React from 'react'
import { Col, Row } from 'react-bootstrap';

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

interface Props {
    data: ConversionsI,
    heading: string
}

interface Dictionary {
    [key: string]: string;
}

type conversiaAccessors = Array<keyof ConversionsI>

const IndicatorsTableComponent = ({ data, heading }: Props) => {

    const indicatorsNames: Dictionary = {
        'avgPriceRub': 'Средняя цена, руб.',
        'ordersCount': 'Заказали, шт.',
        'ordersSumRub': 'Заказали, руб.',
        'buyoutsCount': 'Выкупили, шт.',
        'buyoutsSumRub': 'Выкупили, руб.',
        'cancelCount': 'Отменили, шт.',
        'cancelSumRub': 'Отменили, руб.'
    }
    const myTableStyle = {
        marginTop: 15,
        marginRight: 10,
        marginLeft: 10,
        marginBottom: 20,
    }

    return (
        <>
            <div style={{ textAlign: 'center' }}>
                <h2>{heading}</h2>
            </div>
            <div style={myTableStyle}>
                <table className='table table-bordered'>
                    <tbody>
                        {(Object.keys(indicatorsNames) as conversiaAccessors).map((indicator) =>
                            <tr>
                                <td>
                                    <>{indicatorsNames[indicator]}</>
                                </td>
                                <td>
                                    <>{data[indicator]}</>
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </>
    )
}

export default IndicatorsTableComponent