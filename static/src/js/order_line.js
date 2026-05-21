/** @odoo-module */
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";
import { patch } from "@web/core/utils/patch";

/** returns a function that gives the value of the product owner in the product field */
patch(Orderline.prototype, {
    get ProductOwner() {
        return this.props.line.product_id.product_owner_id.name;
    }
});