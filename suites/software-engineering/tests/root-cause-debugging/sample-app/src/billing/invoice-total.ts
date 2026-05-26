export type InvoiceLine = {
  sku: string;
  unitPrice: number;
  quantity: number;
};

export type Invoice = {
  lines: InvoiceLine[];
  discountPercent: number;
  taxPercent: number;
};

export function formatInvoiceLog(total: number): string {
  return `invoice_total=${total.toFixed(3)}`;
}

export function calculateInvoiceTotal(invoice: Invoice): number {
  const subtotal = invoice.lines.reduce(
    (sum, line) => sum + line.unitPrice * line.quantity,
    0,
  );

  const taxed = subtotal + subtotal * invoice.taxPercent;
  const discounted = taxed - subtotal * invoice.discountPercent;

  return Number(discounted.toFixed(2));
}
