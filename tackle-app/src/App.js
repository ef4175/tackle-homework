import React, { Component } from 'react';
import Vendor from './Vendor';
import { getVendors } from './api';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loaded: false,
      vendors: null,
    };
  }
  componentDidMount() {
    this.loadVendors();
  }
  async loadVendors() {
    const vendors = await getVendors();
    this.setState({
      vendors,
      loaded: true,
    });
  }
  render() {
    if (!this.state.loaded) {
      return (
        <div>
          Loading.
        </div>
      );
    }
    const vendorsList = this.state.vendors.map(vendor => {
      return (
        <Vendor
          key={vendor.id}
          id={vendor.id}
          name={vendor.name}
        />
      );
    });
    return (
      <div>
        <h1>Vendors:</h1>
        {vendorsList}
      </div>
    );
  }
}

export default App;
