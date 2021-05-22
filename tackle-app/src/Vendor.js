import React, { Component } from 'react';
import Product from './Product';
import { getProducts } from './api';
import './shared.css';

class Vendor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id: props.id,
      name: props.name,
      loadedProducts: false,
      products: null,
    };
  }
  async handleClick() {
    const products = await getProducts(this.state.id);
    this.setState({
      products,
      loadedProducts: true,
    });
  }
  render() {
    if (!this.state.loadedProducts) {
      return (
        <div onClick={this.handleClick.bind(this)}>
          <h2 className="cursor-pointer-on-hover">{this.state.name}</h2>
        </div>
      );
    }
    const productsList = this.state.products.map(product => {
      return (
        <Product
          key={product.id}
          id={product.id}
          title={product.title}
          listingType={product.listingType}
          price={product.price}
          vendorId={this.state.id}
        />
      );
    });
    return (
      <div>
        <h2 className="cursor-pointer-on-hover">{this.state.name}</h2>
        <h3>Products:</h3>
        <div>
          {productsList}
        </div>
      </div>
    );
  }
}

export default Vendor;
