import React from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';
import { PieLabelRenderProps } from 'recharts';
type DataPoint = {
    name: string;
    value: number;
};
type Props = {
    data: DataPoint[];
};

const PieChartComponent: React.FC<Props> = ({ data }) => {
    const colors: string[] = ['#212C3C', '#3E5F85', '#7F5684', '#FFF779', '#79B7FF']
    //const total = (chartType == "canceledBuyed") ? (data.reduce((sum, item) => sum + item.value, 0)) : (data[0].value);
    const total = data.reduce((sum, item) => sum + item.value, 0)


    const labelrender = (props: PieLabelRenderProps &
    { percent: number, cx: number, cy: number, midAngle: number, innerRadius: number, outerRadius: number, index: number }) => {
        const RADIAN = Math.PI / 180;
        const { cx, cy, midAngle, innerRadius, outerRadius, percent, index } = props;
        const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
        const x = cx + radius * Math.cos(-midAngle * RADIAN);
        const y = cy + radius * Math.sin(-midAngle * RADIAN);

        // return (
        //     <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central">
        //         {`${(percent * 100).toFixed(0)}% (${data[index].value}/${total})`}
        //     </text>
        // );
        return (
                `${(percent * 100).toFixed(0)}%`
        );
    }

    return (
        <PieChart width={400} height={300}>
            <Pie
                dataKey="value"
                data={data}
                cx="50%"
                cy="50%"
                outerRadius={110}
                fill="#8884d8"
                labelLine={true}
                label={labelrender}>
                {data.map((entry, index) => (
                    <Cell key={`cell-${index}`}
                        fill={colors[index % colors.length]}
                        aria-label={entry + '%'} />
                ))}
            </Pie>
            <Tooltip />
            <Legend />
        </PieChart>);
};
export default PieChartComponent;
