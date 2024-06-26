import { useEffect, useState } from 'react'
import React from 'react'
import SalesDataList from './SalesDataList';
import ReturnsDataList from './ReturnsDataList';
import axios, { CanceledError } from 'axios';
import StorageDataList from './StorageDataList';
import LogisticsDataList from './LogisticsDataList';
import OtherDataList from './OtherDataList';

interface storageObject {
    id: number,
    storaging: number,
    recount_storaging: number,
    acceptanse: number
}

interface logisticsObject {
    id: number,
    number: number,
    amount: number,
    average_price: number,
}

interface OtherI {
    fines: number,
    surchages: number,
    compensation: number
}

interface Dictionary {
    [key: string]: number;
}

const Report = () => {
    const [salesData, setSalesData] = useState<any[]>([])
    const [returnsData, setReturnsData] = useState<any[]>([])
    const [storageData, setStorageData] = useState<Dictionary>({ "": 0 })
    const [logisticsData, setLogisticsData] = useState<any[]>([])
    const [otherData, setOtherData] = useState<OtherI>({ fines: 0, surchages: 0, compensation: 0 })
    const [getsum, setsum] = useState<number>(0)
    const [error, setError] = useState("")
    const endpoint = `${import.meta.env.VITE_API_URL}reports/`
    var totalRow: string[] = []
    var totalArray: number[] = []
    var summa = 0.0

    useEffect(() => {
        const controller = new AbortController();

        axios
            .get<[]>(endpoint + `sales`, { signal: controller.signal })
            .then(res => setSalesData(res.data))
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
            .get<[]>(endpoint + `returns`, { signal: controller.signal })
            .then(res =>
                setReturnsData(res.data))
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
            .get<OtherI[]>(endpoint + `other`, { signal: controller.signal })
            .then(res =>
                setOtherData(res.data[0])
            )
            // setOtherData(res.data))
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
            .get<storageObject[]>(endpoint + `storage`, { signal: controller.signal })
            .then(res => {
                res.data.map(r => {
                    setStorageData({
                        "Хранение": r.storaging,
                        "Пересчет хранения": r.recount_storaging,
                        "Платная приемка": r.acceptanse
                    })
                })
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
            .get<logisticsObject[]>(endpoint + `logistics`, { signal: controller.signal })
            .then(res => {
                var temp: {
                    number: number,
                    average_price: number,
                    amount: number
                }[] = []
                res.data.map(r => {
                    temp.push({
                        number: r.number,
                        average_price: r.average_price,
                        amount: r.amount
                    })
                }
                )
                setLogisticsData(temp)
            }
            )
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );

        return () => controller.abort()

    }, [])

    const setTotalRow = (sum: number, total: string) => {
        summa = summa + sum
        setsum(summa)
        console.log(summa)
        totalRow.push(total)
        totalArray.push(sum)
    }

    return (<>
        <h1>Отчет за прошедшую неделю</h1>
        <h3>Продажи</h3>
        <SalesDataList sales={salesData} getTotal={setTotalRow} />
        <h3>Возвраты</h3>
        <ReturnsDataList returns={returnsData} getTotal={setTotalRow} />
        <h3>Склад</h3>
        <StorageDataList items={storageData} getTotal={setTotalRow} />
        <h3>Логистика</h3>
        <LogisticsDataList items={logisticsData} getTotal={setTotalRow} />
        <h3>Другое</h3>
        {console.log(otherData)}
        <OtherDataList
            fines={otherData.fines}
            surchages={otherData.surchages}
            compensation={otherData.compensation}
            getTotal={setTotalRow} />
        <table className='table myFormat'>
            <tr>
            <td>Итого</td>
            <td>{getsum}</td>
            </tr>
        </table>
    </>
    )
}

export default Report