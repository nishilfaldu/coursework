import * as d3 from "d3";

import { processCountiesData } from "./data";

/**
 * CentralDataStore — the hub for linked brushing. Charts subscribe to it; when
 * one chart brushes a selection it calls updateData(), and every subscriber is
 * notified via update() to highlight the same set of counties.
 */
export class CentralDataStore {
    constructor(_attribute) {
        this.sharedData = [];
        this.subscribers = [];
        this.attribute = _attribute;

        d3.csv("data/national_health_data.csv").then((data) => {
            const processedData = processCountiesData(data);
            const filteredData = processedData.filter(
                (d) => d[_attribute] !== -1,
            );

            this.sharedData = filteredData.map((cnty) => cnty.cnty_fips);
        });
    }

    updateData(data) {
        this.sharedData = data;
        this.notifySubscribers();
    }

    subscribe(subscriber) {
        this.subscribers.push(subscriber);
    }

    getData() {
        return this.sharedData;
    }

    notifySubscribers() {
        this.subscribers.forEach((subscriber) => {
            subscriber.update(this.sharedData);
        });
    }
}

// export const centralDataStore = new CentralDataStore();
