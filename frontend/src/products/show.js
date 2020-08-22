import React, { useState, useEffect } from "react";
import axios from "axios";
import { Spin, Descriptions } from 'antd';
import { useParams } from "react-router-dom";

const Product = (props) => {
  const [isLoading, setIsLoading] = useState(true);
  const [product, setProduct] = useState([]);
  let { id } = useParams();

  useEffect(
    () => {
      axios.get(`http://backend:5001/products/${id}`).then((res) => {
        setProduct(res.data.product);
        setIsLoading(false);
      })
    },
    []
  );

  return (
    isLoading ? <Spin /> :
      <Descriptions title="Product Info" layout="vertical">
        <Descriptions.Item label="Name">{product.name}</Descriptions.Item>
        <Descriptions.Item label="Description">{product.description}</Descriptions.Item>
      </Descriptions>
  )
}

export default Product