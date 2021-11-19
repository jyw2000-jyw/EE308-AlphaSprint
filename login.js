Page({

  /**
   * 页面的初始数据
   */
  data: {
      phone:"",
      code:"",
      datalist:""
  },
  bindPhone:function(e){
    this.setData({phone:e.detail.value});
  },
  bindCode:function(e){
    this.setData({code:e.detail.value});
  },
  login:function(){
    console.log(this.data.phone, this.data.code);
    wx.request({
      url: 'http://127.0.0.1:8000/api/login/',
     // ',
      data:{phone: this.data.code, code:this.data.phone},
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