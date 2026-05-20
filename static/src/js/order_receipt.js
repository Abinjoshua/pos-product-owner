/** @odoo-module */
import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { patch } from "@web/core/utils/patch";

patch(OrderReceipt.prototype, {

    get defaultcode() {
        const orderlines_len = this.props.order.getOrderlines().length;
        console.log(1234,orderlines_len)
        for (let i = 0; i < orderlines_len; i++) {
            console.log(this.props.order.lines[i].product_id.default_code)
        }
        return this.props.order.lines[0].product_id.default_code;
    }
});