import axios, { CanceledError } from 'axios';
import React, { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import { Validate } from 'react-hook-form';

interface InfoI {
    nmID: number
}

interface RealPriceI {
    salesCount: number,
    month: number,
    item: number,
}
type Props = {
    info: InfoI;
    heading: string
};

const ProfitCounterComponent: React.FC<Props> = ({ info, heading }) => {
    const [inputValue, setInputValue] = useState('');
    const [resultValue, setResultValue] = useState<RealPriceI>({
        salesCount: 0,
        month: 0,
        item: 0,
    })
    const endpoint = `${import.meta.env.VITE_API_URL}productItemData/`
    const myTableStyle = {
        marginTop: 15,
        marginRight: 10,
        marginLeft: 10,
        marginBottom: 20,
    }


    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (Number(e.target.value) > 0){
            setInputValue(e.target.value);
        } else {
            e.target.value = ""
        }
    }

    const handleButtonClick = () => {
        const controller = new AbortController();

        axios
            .post<RealPriceI>(endpoint + 'getRealPrice/', info, { signal: controller.signal })
            .then(res => {
                const profitItem = res.data.item - parseInt(inputValue);
                const profitMonth = res.data.month - (parseInt(inputValue) * res.data.salesCount);
                setResultValue({
                    salesCount: res.data.salesCount,
                    month: profitMonth,
                    item: profitItem
                });
            })
            .catch(err => {
                if (err instanceof CanceledError) return;
                setError(err.message)
            }
            );
        return () => controller.abort()
    }

    return (
        <Container>
            <div style={{ textAlign: 'center' }}>
                <h2>{heading}</h2>
            </div>
            {/* <form onSubmit={handleSubmit}> */}
            <div className="mb-3" >
                <label htmlFor="inputVal" className="form-label">Введите себестоимость</label>
                <input
                    type="number"
                    //value={inputValue}
                    min="0"
                    onChange={handleInputChange}
                    id="inputVal"
                    className="form-control" />
            </div>
            <button className="btn btn-primary" onClick={handleButtonClick}>Рассчитать прибыль</button>
            <div style={myTableStyle}>
                <table className='table table-bordered'>
                    <tbody>
                        <tr key={0}>
                            <td>Прибыль за месяц</td>
                            <td>{resultValue.month.toFixed(2)}</td>
                        </tr>
                        <tr key={1}>
                            <td>Прибыль за единицу товара</td>
                            <td>{resultValue.item.toFixed(2)}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            {/* </form> */}
        </Container>
    )
}

export default ProfitCounterComponent

function setError(message: any) {
    throw new Error('Function not implemented.' + message);
}


