import axios, { CanceledError } from 'axios';
import React, { useEffect, useState } from 'react'

interface returnItem {
    id: number,
    nm_id: number,
    product_name: string,
    refund_amount: number
}

interface Props {
    returns: returnItem[],
    getTotal: (sum: number, total: string) => void;
}


const ReturnsDataList = ({ returns, getTotal }: Props) => {
    var sum: number = (-1)*returns.reduce((acc, ret) => ret.refund_amount + acc, 0)
    const total: string = sum.toFixed(2)
    getTotal(sum, total)
    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th>Артикул</th>
                    <th>Наименование товара</th>
                    <th>Сумма к возврату</th>
                </tr>
            </thead>
            <tbody>
                {returns.map(ret => <tr key={ret.id}>
                    <td>{ret.nm_id}</td>
                    <td>{ret.product_name}</td>
                    <td>{ret.refund_amount}</td>
                </tr>)}
            </tbody>
            <tfoot>
                <tr>
                    <th>Total</th>
                    <td></td>
                    <th>{total}</th>
                </tr>
            </tfoot>

        </table>
    )
}

export default ReturnsDataList