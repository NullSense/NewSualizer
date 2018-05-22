"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var extend = function (child, parent) { for (var key in parent) {
    if (hasProp.call(parent, key))
        child[key] = parent[key];
} function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; }, hasProp = {}.hasOwnProperty;
var $ = require("jquery");
require("bootstrap/dropdown");
var p = require("core/properties");
var abstract_button_1 = require("./abstract_button");
var dropdown_template_1 = require("./dropdown_template");
exports.DropdownView = (function (superClass) {
    extend(DropdownView, superClass);
    function DropdownView() {
        return DropdownView.__super__.constructor.apply(this, arguments);
    }
    DropdownView.prototype.template = dropdown_template_1.default;
    DropdownView.prototype.render = function () {
        var $a, $item, i, item, items, label, len, ref, that, value;
        DropdownView.__super__.render.call(this);
        items = [];
        ref = this.model.menu;
        for (i = 0, len = ref.length; i < len; i++) {
            item = ref[i];
            $item = item != null ? ((label = item[0], value = item[1], item), $a = $("<a data-value='" + value + "'>" + label + "</a>"), that = this, $a.click(function (e) {
                return that.set_value($(this).data('value'));
            }), $('<li></li>').append($a)) : $('<li class="bk-bs-divider"></li>');
            items.push($item);
        }
        this.$el.find('.bk-bs-dropdown-menu').append(items);
        this.$el.find('button').val(this.model.default_value);
        this.$el.find('button').dropdown();
        return this;
    };
    DropdownView.prototype.set_value = function (value) {
        this.model.value = value;
        return this.$el.find('button').val(value);
    };
    return DropdownView;
})(abstract_button_1.AbstractButtonView);
exports.Dropdown = (function (superClass) {
    extend(Dropdown, superClass);
    function Dropdown() {
        return Dropdown.__super__.constructor.apply(this, arguments);
    }
    Dropdown.prototype.type = "Dropdown";
    Dropdown.prototype.default_view = exports.DropdownView;
    Dropdown.define({
        value: [p.String],
        default_value: [p.String],
        menu: [p.Array, []]
    });
    Dropdown.override({
        label: "Dropdown"
    });
    return Dropdown;
})(abstract_button_1.AbstractButton);
