
interface saleItem {
    nm_id: number;
    product_name: string;
    real_price: number;
    comission: number;
    income: number;
    id: number
}


interface Props {
    sales: saleItem[],
    getTotal: (sum: number, total: string) => void;
}


const SalesDataList = ({ sales, getTotal }: Props) => {
    const sum: number = sales.reduce((acc, sale) => sale.income + acc, 0)
    var znak: string = (sum == 0) ? '' : '+'
    const total = znak+sum.toFixed(2)
    getTotal(sum, total)

    return (
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th>Артикул</th>
                    <th>Наименование товара</th>
                    <th>Цена продажи</th>
                    <th>Комиссия WB</th>
                    <th>Выручка</th>
                </tr>
            </thead>
            <tbody>
                {sales.map(sale => <tr key={sale.id}>
                    <td>{sale.nm_id}</td>
                    <td>{sale.product_name}</td>
                    <td>{sale.real_price}</td>
                    <td>{sale.comission.toFixed(2)}</td>
                    <td>{sale.income}</td>
                </tr>)}
            </tbody>
            <tfoot>
                <tr>
                    <th>Total</th>
                    <td></td>
                    <td></td>
                    <td></td>
                    <th>{total}</th>
                </tr>
            </tfoot>

        </table>
    )
}

export default SalesDataList