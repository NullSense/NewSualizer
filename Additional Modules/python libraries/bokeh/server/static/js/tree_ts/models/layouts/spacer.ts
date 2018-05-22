var extend1 = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
  hasProp = {}.hasOwnProperty;

import {
  LayoutDOM,
  LayoutDOMView
} from "./layout_dom";

import {
  extend
} from "core/util/object";

export var SpacerView = (function(superClass) {
  extend1(SpacerView, superClass);

  function SpacerView() {
    return SpacerView.__super__.constructor.apply(this, arguments);
  }

  SpacerView.prototype.className = "bk-spacer-box";

  SpacerView.prototype.render = function() {
    SpacerView.__super__.render.call(this);
    if (this.sizing_mode === 'fixed') {
      this.el.style.width = this.model.width + "px";
      return this.el.style.height = this.model.height + "px";
    }
  };

  SpacerView.prototype.get_height = function() {
    return 1;
  };

  return SpacerView;

})(LayoutDOMView);

export var Spacer = (function(superClass) {
  extend1(Spacer, superClass);

  function Spacer() {
    return Spacer.__super__.constructor.apply(this, arguments);
  }

  Spacer.prototype.type = 'Spacer';

  Spacer.prototype.default_view = SpacerView;

  Spacer.prototype.get_constrained_variables = function() {
    var constrained_variables;
    constrained_variables = Spacer.__super__.get_constrained_variables.call(this);
    constrained_variables = extend(constrained_variables, {
      'on-edge-align-top': this._top,
      'on-edge-align-bottom': this._height_minus_bottom,
      'on-edge-align-left': this._left,
      'on-edge-align-right': this._width_minus_right,
      'box-cell-align-top': this._top,
      'box-cell-align-bottom': this._height_minus_bottom,
      'box-cell-align-left': this._left,
      'box-cell-align-right': this._width_minus_right,
      'box-equal-size-top': this._top,
      'box-equal-size-bottom': this._height_minus_bottom,
      'box-equal-size-left': this._left,
      'box-equal-size-right': this._width_minus_right
    });
    return constrained_variables;
  };

  return Spacer;

})(LayoutDOM);
