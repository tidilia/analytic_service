import React from 'react'

interface Props {
    fines: number,
    surchages: number,
    compensation: number,
    getTotal: (sum: number, total: string) => void;
}

const OtherDataList = ({ fines, surchages, compensation, getTotal}: Props) => {
    var sum: number = surchages+compensation-fines
    const znak: string = (sum > 0) ? '+' : '-'
    const total = znak + sum.toFixed(2)
    getTotal(sum, total)

    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th></th>
                    <th>Сумма</th>
                </tr>
            </thead>
            <tbody>
                <tr key={0}>
                    <td>Штрафы</td>
                    <td>{fines}</td>
                </tr>
                <tr key={1}>
                    <td>Доплаты</td>
                    <td>{surchages.toFixed(2)}</td>
                </tr>
                <tr key={2}>
                    <td>Компенсация брака</td>
                    <td>{compensation}</td>
                </tr>
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

export default OtherDataList