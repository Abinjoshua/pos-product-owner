/** @odoo-module */
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

patch(Orderline.prototype, {

    get ProductOwner() {
        return this.props.line.product_id.product_owner_id.name;
    }
});