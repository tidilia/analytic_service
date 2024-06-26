import React from 'react'
interface LogisticsObject {
    number: number,
    amount: number
    average_price: number
}

interface Props {
    items: LogisticsObject[],
    getTotal: (sum: number, total: string) => void;
}

const LogisticsDataList = ({ items, getTotal }: Props) => {
    var sum: number = items.reduce((acc, ret) => ret.amount + acc, 0)
    sum = sum * (-1)
    const total: string = sum.toFixed()

    var keys: string[] = []
    type logisticsAccesors = Array<keyof LogisticsObject>
    getTotal(sum, total)

    const types = ['Доставлено', 'Возвращено'];

    items.map((item) =>
        keys = Object.keys(item))
    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th></th>
                    <th>Количество</th>
                    <th>Средняя цена</th>
                    <th>Сумма</th>
                </tr>
            </thead>
            <tbody>
                {types.map((type, index) =>
                    <tr key={index}>
                        <td>{type}</td>
                        {(keys as logisticsAccesors).map(key =>
                            <td>{items[index][key]}</td>
                        )}
                    </tr>
                )}
            </tbody>
            <tfoot>
                <tr>
                    <th>Total</th>
                    <td></td>
                    <td></td>
                    <th>{total}</th>
                </tr>
            </tfoot>

        </table >
    )
}

export default LogisticsDataList