'use client';

import React, { useState } from 'react';
import AdminSidebar from '@/components/admin/AdminSidebar';
import { useLanguage } from '@/context/LanguageContext';
import { formatPrice } from '@/lib/utils';
import { Settings, Save, Check, MapPin, Phone, ShieldCheck } from 'lucide-react';

export default function AdminSettingsPage() {
  const { locale } = useLanguage();

  const [shippingRates, setShippingRates] = useState([
    { gov: 'القاهرة', fee: 50 },
    { gov: 'الجيزة', fee: 50 },
    { gov: 'الإسكندرية', fee: 60 },
    { gov: 'القليوبية', fee: 60 },
    { gov: 'الشرقية والدقهلية والغربية', fee: 70 },
    { gov: 'مدن القناة (الإسماعيلية، السويس، بورسعيد)', fee: 75 },
    { gov: 'محافظات الصعيد (أسيوط، سوهاج، قنا، أسوان)', fee: 95 },
  ]);

  const [freeShippingThreshold, setFreeShippingThreshold] = useState(10000);
  const [storeHotline, setStoreHotline] = useState('01000000000');
  const [storeAddress, setStoreAddress] = useState('القاهرة، جمهورية مصر العربية');
  const [isSaved, setIsSaved] = useState(false);

  const handleRateChange = (index: number, newFee: number) => {
    const updated = [...shippingRates];
    updated[index].fee = newFee;
    setShippingRates(updated);
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3000);
  };

  return (
    <div className="flex min-h-screen bg-slate-50">
      <AdminSidebar />

      <main className="flex-1 p-6 sm:p-8 space-y-6 overflow-y-auto">
        {/* Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
          <div>
            <h1 className="text-2xl font-black text-petrol-900">إعدادات المتجر والشحن</h1>
            <p className="text-xs text-slate-500 mt-0.5">
              تحديد تسعيرة الشحن لكل محافظة وضبط خيارات الدفع عند الاستلام (COD)
            </p>
          </div>

          <button
            onClick={handleSave}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-petrol-700 hover:bg-petrol-800 text-white font-bold text-xs shadow-xs transition-colors"
          >
            {isSaved ? <Check className="w-4 h-4 text-emerald-300" /> : <Save className="w-4 h-4" />}
            <span>{isSaved ? 'تم الحفظ بنجاح!' : 'حفظ التعديلات'}</span>
          </button>
        </div>

        <div className="max-w-4xl space-y-6">
          {/* Shipping Rates Box */}
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
            <div className="flex items-center justify-between border-b border-slate-100 pb-3">
              <h3 className="font-extrabold text-sm text-petrol-900 flex items-center gap-2">
                <MapPin className="w-4 h-4 text-sky-600" />
                <span>تعريفة الشحن لمحافظات مصر (COD)</span>
              </h3>
            </div>

            <div className="space-y-3">
              {shippingRates.map((rate, idx) => (
                <div
                  key={idx}
                  className="flex items-center justify-between p-3 rounded-xl bg-slate-50/80 border border-slate-100 text-xs"
                >
                  <span className="font-bold text-slate-800">{rate.gov}</span>
                  <div className="flex items-center gap-2">
                    <input
                      type="number"
                      value={rate.fee}
                      onChange={(e) => handleRateChange(idx, Number(e.target.value))}
                      className="w-20 px-2 py-1 text-center font-mono font-bold rounded-lg border border-slate-200 bg-white"
                    />
                    <span className="text-slate-400 font-medium">ج.م</span>
                  </div>
                </div>
              ))}
            </div>

            <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-xs">
              <div>
                <span className="font-bold text-petrol-900 block">حد الشحن المجاني التلقائي:</span>
                <span className="text-slate-400 text-[11px]">أي طلب يتجاوز هذا المبلغ يحصل على شحن مجاني</span>
              </div>
              <div className="flex items-center gap-2">
                <input
                  type="number"
                  value={freeShippingThreshold}
                  onChange={(e) => setFreeShippingThreshold(Number(e.target.value))}
                  className="w-28 px-3 py-1.5 text-center font-mono font-black rounded-lg border border-slate-200 bg-white text-petrol-900"
                />
                <span className="text-slate-400 font-bold">ج.م</span>
              </div>
            </div>
          </div>

          {/* Store Info */}
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-subtle space-y-4">
            <h3 className="font-extrabold text-sm text-petrol-900 border-b border-slate-100 pb-3 flex items-center gap-2">
              <Phone className="w-4 h-4 text-sky-600" />
              <span>بيانات الاتصال وخدمة العملاء</span>
            </h3>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
              <div>
                <label className="block text-slate-600 font-bold mb-1">الخط الساخن / هاتف الدعم:</label>
                <input
                  type="text"
                  value={storeHotline}
                  onChange={(e) => setStoreHotline(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 font-mono"
                />
              </div>

              <div>
                <label className="block text-slate-600 font-bold mb-1">عنوان المقر الإداري:</label>
                <input
                  type="text"
                  value={storeAddress}
                  onChange={(e) => setStoreAddress(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200"
                />
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
