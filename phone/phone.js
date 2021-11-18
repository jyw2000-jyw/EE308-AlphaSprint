// pages/phone/phone.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      username:"",
      password:"",
      datalist:""
  },
  bindPhone:function(e){
    this.setData({username:e.detail.value});
  },
  bindCode:function(e){
    this.setData({password:e.detail.value});
  },
  login:function(){
    console.log(this.data.username, this.data.password);
    wx.request({
      url: 'http://127.0.0.1:8000/api/login/',
     // ',
      data:{username: this.data.username, password:this.data.password},
      method:'Get',
      header:{
        'content-type':'application/json'
      },
      success:function(res){
        console.log(res)
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */

  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },
  
  
  

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
