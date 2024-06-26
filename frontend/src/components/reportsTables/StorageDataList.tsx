import React from 'react'

interface Dictionary {
    [key: string]: number;
}

interface Props {
    items: Dictionary,
    getTotal: (sum: number, total: string) => void;
}

const StorageDataList = ({ items, getTotal }: Props) => {
    var sum: number
    
    sum = 0.0;

    (Object.keys(items)).map((item) =>{
        if (item == 'Пересчет хранения'){
            sum -= items[item]
        } else {
            sum += items[item]
        }
    })

    sum = sum * (-1)
    var znak: string = (sum > 0) ? '+' : ''
    const total: string = znak+sum.toFixed(2)
    getTotal(sum, total)


    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th>Вид затрат</th>
                    <th>Сумма</th>
                </tr>
            </thead>
            <tbody>
                {(Object.keys(items)).map((item) =>
                    <tr key={item}>
                        <td>
                            <>{item}</>
                        </td>
                        <td>
                            <>{items[item]}</>
                        </td>
                    </tr>
                )}
            </tbody>
            <tfoot>
                <tr>
                    <th>Total</th>
                    <th>{total}</th>
                </tr>
            </tfoot>

        </table>
    )
}

export default StorageDataList