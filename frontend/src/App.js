import React from 'react';
import './App.css';
import { Layout, Menu } from 'antd';
import Products from './products';
import Product from './products/show';
import ProductForm from './products/form';
import history from './history';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
const { Header, Content, Footer } = Layout;

console.log("history", history);

function App() {
  return (
    <Router history={history}>
      <Layout className="layout">
        <Header>
          <div className="logo" />
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
            <Menu.Item key="1"><Link to="/products">Products</Link></Menu.Item>
          </Menu>
        </Header>
        <Content style={{ padding: '50px' }}>
          <div className="site-layout-content">
            <Switch>
              <Route path="/products/new">
                <ProductForm />
              </Route>
              <Route path="/products/:id">
                <Product />
              </Route>
              <Route path="/products">
                <Products />
              </Route>
              <Route path="/">
                Welcome!
              </Route>
            </Switch>
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
      </Layout>
    </Router>
  );
}

export default App;
