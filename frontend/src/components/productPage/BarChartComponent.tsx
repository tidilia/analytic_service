import React from 'react'
import { BarChart, Bar, Rectangle, XAxis, YAxis, CartesianGrid, Tooltip, Legend, Cell } from 'recharts';

type DataPoint = {
    name: number | string;
    value: number;
};

type Props = {
    data: DataPoint[];
    heading: string
};


const BarChartComponent: React.FC<Props> = ({ data, heading }) => {
    const colors: string[] = ['#212C3C', '#3E5F85', '#7F5684', '#FFF779', '#79B7FF']
    return (
        <>
            <div style={{ textAlign: 'center' }}>
                <h2>{heading}</h2>
            </div>
            <BarChart
                width={600}
                height={300}
                data={data}
                margin={{
                    top: 5,
                    right: 50,
                    left: 0,
                    bottom: 5,
                }}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#8884d8" activeBar={<Rectangle fill="pink" stroke="blue" />} >
                    {data.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={colors[index % 20]} width={30} />
                    ))}
                </Bar>
            </BarChart>
        </>

    )
}

export default BarChartComponent