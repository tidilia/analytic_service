
import React from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

type DataPoint = {
    name: number | string;
    value: number;
};

type Props = {
    data: DataPoint[];
    chartType: string;
    heading: string
};



const ChartComponent: React.FC<Props> = ({ data, chartType, heading }) => {
    const timeLabel: string = (chartType == 'week') ? 'Дни недели' : 'Время'
    const total = data.reduce((sum, item) => sum + item.value, 0)
    return (
        <>
            <div style={{ textAlign: 'center' }}>
                <h2>{heading + ' - ' +total }</h2>
            </div>
            <LineChart
                width={630}
                height={300}
                data={data}
                margin={{
                    top: 15,
                    right: 20,
                    left: 10,
                    bottom: 20,
                }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" label={{ value: timeLabel, position: 'insideBottom', offset: -15 }} />
                <YAxis label={{ value: 'Кол-во заказов', position: 'insideLeft', angle: -90 }} />
                <Tooltip />
                {/* <Legend /> */}
                <Line type="monotone" dataKey="value" stroke="#8884d8" />
            </LineChart >
        </>);
};
export default ChartComponent;
