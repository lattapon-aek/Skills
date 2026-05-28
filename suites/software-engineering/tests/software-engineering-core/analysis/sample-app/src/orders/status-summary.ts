export type OrderStatus = "PENDING" | "PAID" | "CANCELLED" | "REFUNDED";

export type Order = {
  id: string;
  status: OrderStatus;
};

export function countActiveOrders(orders: Order[]): number {
  return orders.filter((order) => order.status !== "REFUNDED").length;
}

export function summarizeOrderHealth(orders: Order[]): string {
  const activeCount = countActiveOrders(orders);
  return `Active orders: ${activeCount}`;
}
