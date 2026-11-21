'use client';

import React, { useState, Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import { useLanguage } from '@/context/LanguageContext';
import { Search, CheckCircle2, PackageCheck, Truck, Clock, MapPin } from 'lucide-react';

function TrackOrderInner() {
  const searchParams = useSearchParams();
  const { t } = useLanguage();

  const initialOrder = searchParams.get('order') || 'MESS-842910';
  const initialPhone = searchParams.get('phone') || '01012345678';

  const [orderId, setOrderId] = useState(initialOrder);
  const [phone, setPhone] = useState(initialPhone);
  const [searched, setSearched] = useState(true);

  const steps = [
    {
      title: 'تم تأكيد الطلب',
      desc: 'تم تسجيل بيانات الطلب وحجز المنتجات من المستودع',
      time: 'اليوم، 02:15 م',
      completed: true,
      current: false,
      icon: <CheckCircle2 className="w-5 h-5 text-emerald-600" />,
    },
    {
      title: 'قيد التجهيز والتغليف',
      desc: 'فحص سلامة السيريالات والتغليف الآمن للشحن',
      time: 'اليوم، 04:30 م',
      completed: true,
      current: false,
      icon: <PackageCheck className="w-5 h-5 text-emerald-600" />,
    },
    {
      title: 'خرج مع مندوب التوصيل',
      desc: 'الشحنة مع مندوب شركة الشحن في طريقها إليك',
      time: 'متوقع غداً خلال ساعات العمل',
      completed: false,
      current: true,
      icon: <Truck className="w-5 h-5 text-sky-600" />,
    },
    {
      title: 'تم التسليم والدفع',
      desc: 'معاينة الطلب وسداد القيمة نقداً لمندوب الشحن (COD)',
      time: 'خطوة قادمة',
      completed: false,
      current: false,
      icon: <Clock className="w-5 h-5 text-slate-300" />,
    },
  ];

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      <div className="text-center space-y-2">
        <h1 className="text-2xl sm:text-3xl font-black text-petrol-900">{t('trackOrder')}</h1>
        <p className="text-xs sm:text-sm text-slate-500">
          تابع مسار شحنتك لحظة بلحظة حتى باب البيت أو مقر شركتك
        </p>
      </div>

      {/* Search Tracker Card */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
          <input
            type="text"
            value={orderId}
            onChange={(e) => setOrderId(e.target.value)}
            placeholder="رقم الطلب (مثال: MESS-842910)"
            className="w-full px-4 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
          />
          <input
            type="tel"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            placeholder="رقم الهاتف المسجل بالطلب"
            className="w-full px-4 py-2.5 text-xs rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-petrol-500 font-mono"
          />
          <button
            onClick={() => setSearched(true)}
            className="w-full py-2.5 px-4 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs flex items-center justify-center gap-2"
          >
            <Search className="w-4 h-4" />
            <span>بحث وتتبع</span>
          </button>
        </div>
      </div>

      {searched && (
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-subtle space-y-8">
          {/* Order Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 pb-5">
            <div>
              <span className="text-[11px] font-mono text-slate-400 block">رقم الشحنة</span>
              <h3 className="text-lg font-black text-petrol-900 font-mono">{orderId}</h3>
            </div>
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 rounded-full bg-sky-50 text-sky-700 font-bold text-xs border border-sky-200 flex items-center gap-1.5">
                <Truck className="w-3.5 h-3.5" />
                <span>خرج مع المندوب للتسليم</span>
              </span>
            </div>
          </div>

          {/* Stepper Timeline */}
          <div className="relative space-y-8 ps-6 sm:ps-8 before:absolute before:top-3 before:bottom-3 before:start-2.5 before:w-0.5 before:bg-slate-200">
            {steps.map((step, idx) => (
              <div key={idx} className="relative flex items-start gap-4">
                <div
                  className={`absolute -start-6 sm:-start-8 top-0.5 w-6 h-6 rounded-full flex items-center justify-center bg-white border-2 ${
                    step.completed
                      ? 'border-emerald-500 text-emerald-500'
                      : step.current
                      ? 'border-sky-500 text-sky-500 ring-4 ring-sky-100'
                      : 'border-slate-300 text-slate-300'
                  }`}
                >
                  <div
                    className={`w-2 h-2 rounded-full ${
                      step.completed ? 'bg-emerald-500' : step.current ? 'bg-sky-500' : 'bg-transparent'
                    }`}
                  />
                </div>

                <div className="flex-1 space-y-1">
                  <div className="flex items-center justify-between">
                    <h4
                      className={`font-bold text-sm ${
                        step.completed || step.current ? 'text-petrol-900' : 'text-slate-400'
                      }`}
                    >
                      {step.title}
                    </h4>
                    <span className="text-[11px] font-mono text-slate-400">{step.time}</span>
                  </div>
                  <p className="text-xs text-slate-500 leading-relaxed">{step.desc}</p>
                </div>
              </div>
            ))}
          </div>

          {/* Courier Info Box */}
          <div className="p-4 rounded-2xl bg-petrol-50/70 border border-petrol-100 flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-petrol-700 text-white flex items-center justify-center">
                <MapPin className="w-5 h-5" />
              </div>
              <div>
                <h5 className="font-bold text-xs text-petrol-900">مندوب التوصيل: كابتن أحمد محمود</h5>
                <p className="text-[11px] text-slate-500">شركة شحن ميس تك إكسبريس - القاهرة والجيزة</p>
              </div>
            </div>
            <a
              href="tel:01000000000"
              className="px-4 py-2 rounded-xl bg-white text-petrol-800 font-bold text-xs border border-petrol-200 hover:bg-petrol-100 transition-colors"
            >
              اتصال بالمندوب
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

export default function TrackOrderPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-xs text-slate-400">جاري تحميل بيانات التتبع...</div>}>
      <TrackOrderInner />
    </Suspense>
  );
}
