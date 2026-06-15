/**
 * Shared state store. Holds the currently selected/brushed subset of
 *  sightings and notifies subscribed views so the dashboard's coordinated
 *  views update together (cross-filtering / linked brushing).
 */
export class CentralDataStore {
  constructor(_data) {
    this.sharedData = _data || [];
    this.subscribers = [];
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
