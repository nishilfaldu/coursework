import { Select } from "antd";
import dynamic from "next/dynamic";
import { Inter } from "next/font/google";
import { useState } from "react";

import { BarChart } from "@/components/Charts/BarChart";
import { Choropleth } from "@/components/Charts/ChoroplethMap";
import { ScatterPlot } from "@/components/Charts/ScatterPlot";
import { Navbar } from "@/components/Navbar";
import { CentralDataStore } from "@/lib/CentralDataStore";
import { attributesInfoArray } from "@/lib/data";

// The D3 charts manipulate the DOM directly, so they are loaded client-side only.
const DynamicBarChart = dynamic(() => Promise.resolve(BarChart), {
    ssr: false,
});
const DynamicChoropleth = dynamic(() => Promise.resolve(Choropleth), {
    ssr: false,
});
const DynamicScatterPlot = dynamic(() => Promise.resolve(ScatterPlot), {
    ssr: false,
});

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
    const [selectedFirst, setSelectedFirst] = useState<string>(
        attributesInfoArray[0].value,
    );
    const [selectedSecond, setSelectedSecond] = useState<string>(
        attributesInfoArray[0].value,
    );

    const centralDataStore = new CentralDataStore(selectedFirst);

    const handleChangeFirst = (value: string) => {
        setSelectedFirst(value);
    };

    const handleChangeSecond = (value: string) => {
        setSelectedSecond(value);
    };

    return (
        <main
            className={`container flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
        >
            <Navbar />

            <div className="flex gap-x-4">
                <span className="flex flex-col">
                    <span>Change X-Attribute</span>
                    <Select
                        defaultValue={attributesInfoArray[0].value}
                        style={{ width: 300 }}
                        onChange={handleChangeFirst}
                        options={attributesInfoArray.map((d) => {
                            return { value: d.value, label: d.label };
                        })}
                        size="large"
                    />
                </span>
                <span className="flex flex-col">
                    <span>Change Y-Attribute</span>
                    <Select
                        defaultValue={attributesInfoArray[0].value}
                        style={{ width: 300 }}
                        onChange={handleChangeSecond}
                        options={attributesInfoArray.map((d) => {
                            return { value: d.value, label: d.label };
                        })}
                        size="large"
                    />
                </span>
            </div>
            <div className="flex flex-row">
                <DynamicBarChart
                    dataUrl={"/data/national_health_data.csv"}
                    attribute={selectedFirst}
                    dataStore={centralDataStore}
                />
                <DynamicScatterPlot
                    dataUrl={"/data/national_health_data.csv"}
                    xAttribute={selectedFirst}
                    yAttribute={selectedSecond}
                    dataStore={centralDataStore}
                />
            </div>
            <div className="flex flex-row">
                <DynamicChoropleth
                    dataUrl={"/data/national_health_data.csv"}
                    attribute={selectedFirst}
                    num={1}
                    dataStore={centralDataStore}
                />
                <DynamicChoropleth
                    dataUrl={"/data/national_health_data.csv"}
                    attribute={selectedSecond}
                    num={2}
                    dataStore={centralDataStore}
                />
            </div>
        </main>
    );
}
