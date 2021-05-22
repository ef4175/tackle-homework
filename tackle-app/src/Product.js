import React, { Component } from 'react';
import { getOrders } from './api';
import './shared.css';

class Product extends Component {
  constructor(props) {
    super(props)
    this.state = {
      id: props.id,
      title: props.title,
      listingType: props.listingType,
      price: props.price,
      vendorId: props.vendorId,
      loadedOrders: false,
      orders: null,
    };
  }
  async handleClick() {
    const orders = await getOrders(this.state.vendorId, this.state.id);
    this.setState({
      orders,
      loadedOrders: true,
    });
  }
  render() {
    if (!this.state.loadedOrders) {
      return (
        <div onClick={this.handleClick.bind(this)}>
          <h4 className="cursor-pointer-on-hover">{this.state.title}</h4>
        </div>
      );
    }
    const ordersList = this.state.orders.map(order => {
      return (
        <div
          key={order.id}
        >
          <p>Ordered on {order.orderDate} by {order.fullName}</p>
        </div>
      );
    });
    return (
      <div>
        <h4 className="cursor-pointer-on-hover">{this.state.title}</h4>
        <p>Revenue: {this.state.price * this.state.orders.length}</p>
        <h5>Orders:</h5>
        <div>
          {ordersList}
        </div>
      </div>
    );
  }
}

export default Product;
